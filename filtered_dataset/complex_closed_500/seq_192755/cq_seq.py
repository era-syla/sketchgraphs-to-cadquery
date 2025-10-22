import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.07, -0.03).lineTo(-0.19, -0.03).lineTo(-0.19, -0.095).lineTo(0.07, -0.095).lineTo(0.07, -0.03).close()
solid=wp_sketch0.add(loop0).extrude(-0.045460245723583086)
