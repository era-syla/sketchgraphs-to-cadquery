import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -0.11937).lineTo(0.0381, -0.11937).lineTo(0.0381, -0.62737).lineTo(0.0, -0.62737).lineTo(0.0, -0.11937).close()
solid=wp_sketch0.add(loop0).extrude(-0.18984672116043175)
