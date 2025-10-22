import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0127, -0.02794).lineTo(-0.0127, -0.02794).lineTo(-0.0127, -0.02159).lineTo(0.0127, -0.02159).lineTo(0.0127, -0.02794).close()
solid=wp_sketch0.add(loop0).extrude(-0.001468723430604614)
