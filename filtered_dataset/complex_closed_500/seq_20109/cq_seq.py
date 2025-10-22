import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03, 0.0379).lineTo(-0.03, -0.03798).lineTo(0.03, -0.03798).lineTo(0.03, 0.0379).lineTo(-0.03, 0.0379).close()
solid=wp_sketch0.add(loop0).extrude(0.01706459740132732)
