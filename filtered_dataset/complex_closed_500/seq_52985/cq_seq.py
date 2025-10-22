import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01221, 0.0817).lineTo(0.01221, -0.0183).lineTo(0.05221, -0.0183).lineTo(0.05221, -0.0133).lineTo(0.01721, -0.0133).lineTo(0.01721, 0.08178).lineTo(0.01221, 0.0817).close()
solid=wp_sketch0.add(loop0).extrude(-0.27674545664163175)
