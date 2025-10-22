import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00204, 0.00447).lineTo(0.00194, 0.00447).lineTo(0.00194, 0.00725).lineTo(0.00187, 0.00853).lineTo(-0.00204, 0.00853).lineTo(-0.00204, 0.00722).lineTo(-0.00204, 0.00447).close()
solid=wp_sketch0.add(loop0).extrude(-0.0014875374151192258)
