import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00792, 0.041).lineTo(0.02408, 0.041).lineTo(0.03217, 0.027).lineTo(0.02408, 0.013).lineTo(0.00792, 0.013).lineTo(-0.00017, 0.027).lineTo(0.00792, 0.041).close()
solid=wp_sketch0.add(loop0).extrude(-0.03677212630176695)
