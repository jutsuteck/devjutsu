import { FC } from "react";
import Button from "../ui/Button";

interface Props {
  projectName: string;
  pageName: string;
  hasButton?: boolean;
  buttonText?: string;
  isScrum?: boolean;
  scrumHeader?: string;
  onClick?: () => void;
}

const Header: FC<Props> = ({
  projectName,
  pageName,
  hasButton,
  buttonText,
  scrumHeader,
  onClick,
}) => {
  return (
    <div className="flex justify-between">
      <div>
        <h2 className="text-sm text-nord-polar-night-light mb-4">
          Projects /{" "}
          {projectName?.charAt(0).toUpperCase() + projectName?.slice(1)} /{" "}
          {pageName}
          {scrumHeader && (
            <span className="font-semibold"> {`/ Sprint ${scrumHeader}`}</span>
          )}
        </h2>
        <h1 className="text-4xl font-extrabold">
          {projectName?.charAt(0).toUpperCase() + projectName?.slice(1)}
        </h1>
      </div>
      {hasButton && (
        <div className="self-end">
          <Button text={buttonText} onClick={onClick} />
        </div>
      )}
    </div>
  );
};

export default Header;
