import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.06896, -0.07).lineTo(0.07146, -0.07).lineTo(0.07146, -0.0625).lineTo(0.06896, -0.0625).lineTo(0.06896, -0.07).close()
solid=wp_sketch0.add(loop0).extrude(0.01742179477109292)
