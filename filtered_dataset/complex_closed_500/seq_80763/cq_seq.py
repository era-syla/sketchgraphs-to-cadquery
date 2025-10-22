import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0375, -0.00474).lineTo(0.06806, -0.00474).lineTo(0.06806, -0.01474).lineTo(0.0375, -0.01474).lineTo(0.0375, -0.00474).close()
solid=wp_sketch0.add(loop0).extrude(-0.009839920474166776)
