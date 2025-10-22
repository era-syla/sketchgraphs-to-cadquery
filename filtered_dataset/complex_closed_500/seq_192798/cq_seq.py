import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0135, 0.013).lineTo(0.0135, 0.013).lineTo(0.0135, 0.003).lineTo(-0.0135, 0.003).lineTo(-0.0135, 0.013).close()
solid=wp_sketch0.add(loop0).extrude(-0.05181343901184513)
