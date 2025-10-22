import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.14605, -0.02067).lineTo(-0.127, -0.02067).lineTo(-0.127, -0.0636).lineTo(-0.14605, -0.0636).lineTo(-0.14605, -0.02067).close()
solid=wp_sketch0.add(loop0).extrude(0.01588055767794144)
