"""Ajout de date_updated

Revision ID: bc7a05f3fa73
Revises: 2f82281a9d83
Create Date: 2021-08-16 14:46:06.984893

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bc7a05f3fa73'
down_revision = '2f82281a9d83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signalement', sa.Column('date_updated', sa.DateTime(), nullable=True))
    op.drop_column('signalement', 'sous_categorie')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signalement', sa.Column('sous_categorie', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255), nullable=True))
    op.drop_column('signalement', 'date_updated')
    # ### end Alembic commands ###
