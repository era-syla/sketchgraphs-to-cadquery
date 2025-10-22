import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.21, 0.46039).lineTo(-0.31, 0.46039).lineTo(-0.31, 0.42852).lineTo(-0.21, 0.42852).lineTo(-0.21, 0.46039).close()
solid=wp_sketch0.add(loop0).extrude(-0.2198181515410477)
