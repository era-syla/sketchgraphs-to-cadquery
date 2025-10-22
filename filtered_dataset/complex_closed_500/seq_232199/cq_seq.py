import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.014, -0.00635).lineTo(-0.014, -0.00635).lineTo(-0.014, 0.00635).lineTo(0.014, 0.00635).lineTo(0.014, -0.00635).close()
solid=wp_sketch0.add(loop0).extrude(0.009298245745382846)
