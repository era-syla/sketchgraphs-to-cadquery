import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05, -0.05296).lineTo(0.05, -0.05296).lineTo(0.06, 0.05704).lineTo(-0.06, 0.05704).lineTo(-0.05, -0.05296).close()
solid=wp_sketch0.add(loop0).extrude(0.04886485121251514)
