#!/usr/bin/python3
"""changes the name of a State object from
the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    Base.metadata.create_all(engine)

    ses = Session(engine)
    state = ses.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    ses.commit()
    ses.close()
