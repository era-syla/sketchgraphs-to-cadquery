import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04016, -0.1305).lineTo(-0.01984, -0.1305).lineTo(-0.01984, -0.0955).lineTo(0.04016, -0.0955).lineTo(0.04016, -0.1305).close()
solid=wp_sketch0.add(loop0).extrude(-0.07860090185440001)
