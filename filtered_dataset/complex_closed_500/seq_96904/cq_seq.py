import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00471, -0.05183).lineTo(-0.01462, -0.05183).lineTo(-0.01462, -0.0645).lineTo(0.00471, -0.0645).lineTo(0.00471, -0.05183).close()
solid=wp_sketch0.add(loop0).extrude(0.026854075988642704)
