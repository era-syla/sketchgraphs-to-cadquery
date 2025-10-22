import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-3.0325, 0.0).lineTo(-3.0425, 0.0).lineTo(-3.0425, 2.0).lineTo(-3.0325, 2.0).lineTo(-3.0325, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(2.8654492289104105)
