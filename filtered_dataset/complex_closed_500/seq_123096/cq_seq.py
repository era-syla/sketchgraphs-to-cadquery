import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-4e-05, 0.00418).lineTo(0.00368, -0.00227).lineTo(-0.00377, -0.00227).lineTo(-4e-05, 0.00418).close()
solid=wp_sketch0.add(loop0).extrude(-0.008678049886895845)
