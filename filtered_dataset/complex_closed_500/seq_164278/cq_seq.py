import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01643, 0.01236).lineTo(-0.01239, 0.01236).lineTo(-0.01239, -0.0123).lineTo(-0.01643, -0.0123).lineTo(-0.01643, 0.01236).close()
solid=wp_sketch0.add(loop0).extrude(0.04674247241419927)
