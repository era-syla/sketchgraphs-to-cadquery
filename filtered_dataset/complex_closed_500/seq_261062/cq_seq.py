import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02896, 0.00525).lineTo(0.04486, 0.00525).lineTo(0.04486, -0.0012).lineTo(0.02896, -0.0012).lineTo(0.02896, 0.00525).close()
solid=wp_sketch0.add(loop0).extrude(-0.03534263724737993)
