import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.38054, -0.09591).lineTo(-0.63054, -0.09591).lineTo(-0.63054, -0.09391).lineTo(-0.38054, -0.09391).lineTo(-0.38054, -0.09591).close()
solid=wp_sketch0.add(loop0).extrude(-0.009818243526833914)
