import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(2.0, 0.0).lineTo(2.0, 1.0).lineTo(-0.0, 1.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-2.3684951581819345)
