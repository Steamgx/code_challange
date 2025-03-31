from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'initial_migration'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create heroes table
    op.create_table(
        'heroes',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('super_name', sa.String(), nullable=False)
    )
    
    # Create powers table
    op.create_table(
        'powers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False)
    )
    
    # Create hero_powers table
    op.create_table(
        'hero_powers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('strength', sa.String(), nullable=False),
        sa.Column('hero_id', sa.Integer(), sa.ForeignKey('heroes.id'), nullable=False),
        sa.Column('power_id', sa.Integer(), sa.ForeignKey('powers.id'), nullable=False)
    )

def downgrade():
    op.drop_table('hero_powers')
    op.drop_table('powers')
    op.drop_table('heroes')
