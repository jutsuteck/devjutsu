import { FC, Fragment } from "react";
import { Menu, Transition } from "@headlessui/react";
import { ChevronDownIcon } from "@heroicons/react/20/solid";

interface DropdownProps {
  options: string[];
  onSelect: (selectedOption: string | null) => void;
  label: string;
}

const CustomDropdown: FC<DropdownProps> = ({ label, options, onSelect }) => {
  return (
    <Menu as="div" className="relative inline-block text-left mb-4">
      <div>
        <Menu.Button className="inline-flex w-full justify-center gap-x-1.5 rounded-md bg-nord-polar-night-darkest p-2 hover:bg-gray-50">
          {label}
          <ChevronDownIcon
            className="-mr-1 h-5 w-5 text-gray-400"
            aria-hidden="true"
          />
        </Menu.Button>
      </div>

      <Transition
        as={Fragment}
        enter="transition ease-out duration-100"
        enterFrom="transform opacity-0 scale-95"
        enterTo="transform opacity-100 scale-100"
        leave="transition ease-in duration-75"
        leaveFrom="transform opacity-100 scale-100"
        leaveTo="transform opacity-0 scale-95"
      >
        <Menu.Items className="absolute z-10 mt-2 w-56 rounded-md bg-nord-polar-night-darkest p-2">
          <div className="py-1">
            {options.map((option) => (
              <Menu.Item key={option}>
                {({ active }) => (
                  <button
                    onClick={() => onSelect(option)}
                    className={`${
                      active
                        ? "bg-nord-polar-night-light text-nord-snowstorm-light"
                        : ""
                    }
                      ${"block w-full px-4 py-2 text-left text-sm rounded-md"}`}
                  >
                    {option}
                  </button>
                )}
              </Menu.Item>
            ))}
          </div>
        </Menu.Items>
      </Transition>
    </Menu>
  );
};
export default CustomDropdown;
