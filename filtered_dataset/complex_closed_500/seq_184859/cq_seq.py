import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0315, 0.00935).lineTo(0.0385, 0.00935).lineTo(0.0385, -0.02379).lineTo(0.0315, -0.02379).lineTo(0.0315, 0.00935).close()
solid=wp_sketch0.add(loop0).extrude(0.0013602672873586788)
