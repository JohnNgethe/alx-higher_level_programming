#!/usr/bin/python3
"""adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

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
    new_state = State(name='Louisiana')
    ses.add(new_state)
    state = ses.query(State).filter(State.name == 'Louisiana').first()
    ses.commit()
    print("{}".format(state.id))
    ses.close()
