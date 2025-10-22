import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, -0.0135).lineTo(0.0, -0.0185).lineTo(-0.0002, -0.0185).lineTo(-0.0004, -0.01815).lineTo(-0.0006, -0.0135).lineTo(0.0, -0.0135).close()
solid=wp_sketch0.add(loop0).extrude(-0.013937705541829676)
