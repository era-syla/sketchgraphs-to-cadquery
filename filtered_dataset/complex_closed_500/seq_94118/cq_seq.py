import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0259, 0.0184).lineTo(0.0259, 0.0184).lineTo(0.0259, -0.0184).lineTo(-0.0259, -0.0184).lineTo(-0.0259, 0.0184).close()
solid=wp_sketch0.add(loop0).extrude(0.0019498799239972009)
