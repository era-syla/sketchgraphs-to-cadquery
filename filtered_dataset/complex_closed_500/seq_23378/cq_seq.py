import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.05422).lineTo(0.0, 0.0).lineTo(-0.04159, 0.0).lineTo(-0.00996, 0.05844).lineTo(-0.0, 0.05422).close()
solid=wp_sketch0.add(loop0).extrude(0.08950386695843339)
