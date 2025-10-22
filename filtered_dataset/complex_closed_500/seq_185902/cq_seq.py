import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-1.18155, -0.24986).lineTo(-1.17636, -0.27472).lineTo(-1.1515, -0.26953).lineTo(-1.15669, -0.24467).lineTo(-1.18155, -0.24986).close()
solid=wp_sketch0.add(loop0).extrude(0.03719677354161188)
