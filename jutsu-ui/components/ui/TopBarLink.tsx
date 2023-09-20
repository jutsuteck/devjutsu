import Link from "next/link";
import { useRouter } from "next/router";
import { FC, ReactNode } from "react";

interface Props {
  icon: ReactNode;
  name: string;
  href: string;
}

const TopBarLink: FC<Props> = ({ icon, name, href }) => {
  const router = useRouter();

  const isActive = router.pathname === href;

  const baseStyle =
    "flex items-center justify-center h-full relative p-2 hover:rounded-lg hover:bg-nord-polar-night-dark transition-colors duration-3000";
  const activeRoute = isActive ? "font-extrabold text-nord-frost-light" : "";

  return (
    <Link href={href} className={`${baseStyle} ${activeRoute}`}>
      {icon}
      <span className="ml-2">{name}</span>
    </Link>
  );
};

export default TopBarLink;
