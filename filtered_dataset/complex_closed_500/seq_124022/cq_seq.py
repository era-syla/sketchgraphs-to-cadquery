import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0045, 0.034).lineTo(0.0725, 0.034).lineTo(0.0725, -0.034).lineTo(0.0045, -0.034).lineTo(0.0045, 0.034).close()
solid=wp_sketch0.add(loop0).extrude(0.06976030621258404)
