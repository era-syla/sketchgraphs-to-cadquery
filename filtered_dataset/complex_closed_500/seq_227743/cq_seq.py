import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(2.1625, 1.065).lineTo(2.2225, 1.065).lineTo(2.2225, 1.145).lineTo(2.1625, 1.145).lineTo(2.1625, 1.065).close()
solid=wp_sketch0.add(loop0).extrude(-0.09308010223657186)
