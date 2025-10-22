import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01688, -0.02092).lineTo(0.04212, -0.02092).lineTo(0.04212, 0.00895).lineTo(0.01688, 0.00895).lineTo(0.01688, -0.02092).close()
solid=wp_sketch0.add(loop0).extrude(0.07002289161690664)
