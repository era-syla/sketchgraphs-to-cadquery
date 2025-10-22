import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(1.32251, 0.0).lineTo(-1.24711, 0.0).lineTo(-1.24711, 1.53412).lineTo(1.32251, 1.53412).lineTo(1.32251, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-6.9033579336649895)
