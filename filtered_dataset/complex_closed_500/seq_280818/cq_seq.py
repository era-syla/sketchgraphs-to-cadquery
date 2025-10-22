import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.15673, -0.10917).lineTo(0.07187, -0.10917).lineTo(0.07187, -0.08532).lineTo(-0.15673, -0.08532).lineTo(-0.15673, -0.10917).close()
solid=wp_sketch0.add(loop0).extrude(0.33340377650581754)
