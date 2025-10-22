import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0381, -0.01236).lineTo(0.0, -0.01236).lineTo(0.0, 0.00986).lineTo(-0.0381, 0.00986).lineTo(-0.0381, -0.01236).close()
solid=wp_sketch0.add(loop0).extrude(0.047561564679602326)
