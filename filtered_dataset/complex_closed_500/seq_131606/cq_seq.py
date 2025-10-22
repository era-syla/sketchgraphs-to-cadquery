import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00639, -0.03141).lineTo(0.00377, -0.03141).lineTo(0.00377, -0.03508).lineTo(0.00639, -0.03508).lineTo(0.00639, -0.03141).close()
solid=wp_sketch0.add(loop0).extrude(-0.0015507151021923605)
