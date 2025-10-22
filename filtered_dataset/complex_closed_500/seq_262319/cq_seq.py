import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0017, 0.0122).lineTo(-0.0123, 0.0122).lineTo(-0.0123, 0.0042).lineTo(0.0017, 0.0042).lineTo(0.0017, 0.0122).close()
solid=wp_sketch0.add(loop0).extrude(-0.03744611046018077)
