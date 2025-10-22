import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.29165, 0.3048).lineTo(-0.31795, 0.3048).lineTo(-0.31795, -0.3048).lineTo(0.29165, -0.3048).lineTo(0.29165, 0.3048).close()
solid=wp_sketch0.add(loop0).extrude(0.5855074986239317)
