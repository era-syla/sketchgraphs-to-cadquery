import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(1.8796, -4.02731).lineTo(1.9812, -4.02731).lineTo(1.9812, -3.97651).lineTo(1.8796, -3.97651).lineTo(1.8796, -4.02731).close()
solid=wp_sketch0.add(loop0).extrude(-0.024624529873285474)
