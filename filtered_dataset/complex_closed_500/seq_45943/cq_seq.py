import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00635, -0.0607).lineTo(-0.0, -0.0607).lineTo(0.0, -0.0861).lineTo(0.00635, -0.0861).lineTo(0.00635, -0.0607).close()
solid=wp_sketch0.add(loop0).extrude(0.03673129400115737)
