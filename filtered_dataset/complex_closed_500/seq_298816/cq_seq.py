import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.15946, 0.041).lineTo(0.09646, 0.041).lineTo(0.09646, 0.0).lineTo(0.15946, 0.0).lineTo(0.15946, 0.041).close()
solid=wp_sketch0.add(loop0).extrude(0.028656715520745505)
