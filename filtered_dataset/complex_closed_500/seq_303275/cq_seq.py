import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.1259, -0.01905).lineTo(-0.03446, -0.01905).lineTo(-0.03446, -0.09922).lineTo(0.1259, -0.09922).lineTo(0.1259, -0.01905).close()
solid=wp_sketch0.add(loop0).extrude(0.47973367438925335)
