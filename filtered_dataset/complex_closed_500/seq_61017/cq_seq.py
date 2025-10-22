import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00219, 0.06344).lineTo(-0.01489, 0.06344).lineTo(-0.01489, 0.05074).lineTo(-0.00219, 0.05074).lineTo(-0.00219, 0.06344).close()
solid=wp_sketch0.add(loop0).extrude(0.010357916043832217)
