import Link from "next/link";
import { FC } from "react";

interface Props {
  nameKey: string;
  name: string;
}

const Sidebar: FC<Props> = ({ nameKey, name }) => {
  return (
    <div className="flex flex-col h-full w-64 p-8 space-y-4">
      <div className="space-y-2">
        <h1 className="text-2xl font-bold">{nameKey}</h1>
        <h2 className="tex-lg">{name}</h2>
      </div>
      <hr className="w-3/4 mx-auto border-t border-nord-polar-night-medium" />
      <nav className="flex flex-col space-y-2">
        <Link
          href={`/projects/${nameKey}/journal`}
          className="text-center text-nord-frost-dark font-semibold p-2 rounded-full bg-nord-frost-medium transition-colors duration-200"
        >
          Journal
        </Link>
        <Link
          href={`/projects/${nameKey}/board`}
          className="text-center font-bold p-2 rounded-lg hover:bg-nord-frost-medium transition-colors duration-200"
        >
          Board
        </Link>
      </nav>
    </div>
  );
};

export default Sidebar;
