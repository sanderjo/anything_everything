import asyncio

from datetime import date
from energyzero import EnergyZero #, VatOption

import datetime
print(str(datetime.datetime.today()).split()[0])

from datetime import date
today = str(date.today())
print(today)

async def main() -> None:
    """Show example on fetching the energy prices from EnergyZero."""
    async with EnergyZero() as client:
        start_date = date(2022, 12, 7)
        start_date = date.today()
        end_date = date(2022, 12, 7)
        end_date = date.today()

        energy = await client.energy_prices(start_date, end_date)
        gas = await client.gas_prices(start_date, end_date)

        #print(energy)
        #print(energy.timestamp_prices)
        for i in energy.timestamp_prices:
            #print(i)
            print(i['timestamp'], i['price'])



if __name__ == "__main__":
    asyncio.run(main())
    
