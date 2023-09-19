import Link from "next/link";
import { FC, ReactNode } from "react";

interface Props {
  icon: ReactNode;
  name: string;
  href: string;
}

const TopBarLink: FC<Props> = ({ icon, name, href }) => {
  return (
    <Link
      href={href}
      className="flex items-center justify-center p-2 rounded-lg hover:bg-nord-polar-night-dark transition-colors duration-3000"
    >
      {icon}
      <span className="ml-2">{name}</span>
    </Link>
  );
};

export default TopBarLink;
