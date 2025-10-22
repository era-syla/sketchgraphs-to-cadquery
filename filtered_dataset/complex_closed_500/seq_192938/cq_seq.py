import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0105, 0.003).lineTo(-0.0045, 0.003).lineTo(-0.0045, -0.003).lineTo(-0.0105, -0.003).lineTo(-0.0105, 0.003).close()
solid=wp_sketch0.add(loop0).extrude(0.0047171473342552065)
