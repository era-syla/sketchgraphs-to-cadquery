import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01942, -0.07598).lineTo(0.04456, -0.07598).lineTo(0.04456, -0.07243).lineTo(0.01942, -0.07243).lineTo(0.01942, -0.07598).close()
solid=wp_sketch0.add(loop0).extrude(-0.04431023036267326)
